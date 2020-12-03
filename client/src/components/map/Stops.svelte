<script>
  import { onMount, getContext, createEventDispatcher } from "svelte";
  import { key } from "../../lib/mapbox.js";

  export let name;
  export let id;
  export let modes;

  let filters = [];

  const { getMap, getStops } = getContext(key);
  const map = getMap();
  const stops = getStops();
  const dispatch = createEventDispatcher();

  // FIXME: Best hack ever
  setTimeout(handleFilters, 3500);

  $: id, modes, name, handleFilters();

  function handleFilters() {
    if (!map.isStyleLoaded()) return;
    map.setFilter("layer-stops", null);
    map.setLayoutProperty("layer-stops", "visibility", "visible");
    filters = ["all"];
    getFilterMode() && filters.push(getFilterMode());
    getFilterName() && filters.push(getFilterName());
    getFilterId() && filters.push(getFilterId());
    map.setFilter("layer-stops", filters);
  }

  function getFilterId() {
    if (id && id.length > 0) {
      return ["==", "stop_id", id];
    }
  }

  function getFilterMode() {
    if (modes && modes.length) {
      if (modes.length > 1) {
        return ["!=", "mode", "T"];
      } else {
        return ["==", "mode", modes[0]];
      }
    } else {
      map.setLayoutProperty("layer-stops", "visibility", "none");
    }
  }

  function getFilterName() {
    if (name && name.length > 0) {
      return ["in", "alpha_fr", name];
    }
  }

  onMount(async () => {
    map.on("load", () => {
      map.loadImage("/marker.32px.png", (error, image) => {
        if (error) throw error;
        map.addImage("metro-marker", image);

        map.addSource("source-stops", {
          type: "geojson",
          data: stops,
        });

        map.addLayer({
          id: "layer-stops",
          type: "symbol",
          source: "source-stops",
          minzoom: 10,
          maxzoom: 24,
          layout: {
            visibility: "none",
            "icon-image": "metro-marker",
            "text-field": ["get", "alpha_fr"],
            "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
            "text-offset": [0, 1.25],
            "text-anchor": "top",
          },
        });

        // Remove focus of stop
        map.on("click", () => {
          map.getCanvas().style.cursor = "";
          // Remove the  lines filter and re add other stop markers
          dispatch("select", { line: "null" });
          id = "";
        });

        map.on("click", "layer-stops", (e) => {
          map.getCanvas().style.cursor = "pointer";
          // Filter lines and remove other stop markers
          dispatch("select", {
            line: e.features[0].properties["numero_lig"],
            stop: e.features[0].properties["stop_id"],
            name: e.features[0].properties["alpha_fr"],
          });
          id = e.features[0].properties["stop_id"];
        });
      });
    });
  });
</script>