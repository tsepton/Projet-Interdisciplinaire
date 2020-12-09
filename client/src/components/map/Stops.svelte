<script>
  import { onMount, getContext, createEventDispatcher } from "svelte";
  import { key } from "../../lib/mapbox.js";
  import { lev } from "../../lib/levenstein.js";

  export let name;
  export let line;
  export let mode;

  let filters = [];

  const { getMap, getStops } = getContext(key);
  const map = getMap();
  const stops = getStops();
  const dispatch = createEventDispatcher();
  const names = stops.features.map(
    ({ _, properties }) => properties["alpha_fr"]
  );

  $: mode, line, name, handleFilters();

  function handleFilters() {
    if (map.isStyleLoaded()) {
      map.setFilter("layer-stops", null);
      map.setLayoutProperty("layer-stops", "visibility", "visible");
      filters = ["all"];
      getFilterMode() && filters.push(getFilterMode());
      if (line) getFilterLine() && filters.push(getFilterLine());
      else getFilterName() && filters.push(getFilterName());
      map.setFilter("layer-stops", filters);
    }
  }

  function getFilterMode() {
    if (mode) {
      return ["==", "mode", mode];
    } else {
      map.setLayoutProperty("layer-stops", "visibility", "none");
    }
  }

  function getFilterLine() {
    if (line) {
      return ["==", "numero_lig", line];
    }
  }

  function getFilterName() {
    if (name && name.length > 0) {
      const temp = names.filter(
        (stop) => name === stop || lev(name, stop) <= stop.length / 2
      );
      return ["in", "alpha_fr", ...new Set(temp)];
    }
  }

  onMount(async () => {
    map.on("load", () => {
      map.loadImage("/marker.png", (error, image) => {
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
          dispatch("select", {
            line: undefined,
            stop: undefined,
            name: undefined,
          });
          name = undefined;
          line = undefined;
        });

        map.on("click", "layer-stops", (e) => {
          map.getCanvas().style.cursor = "pointer";
          // Filter lines and remove other stop markers
          dispatch("select", {
            line: e.features[0].properties["numero_lig"],
            stop: e.features[0].properties["stop_id"],
            name: e.features[0].properties["alpha_fr"],
          });
          name = e.features[0].properties["alpha_fr"];
          line = e.features[0].properties["numero_lig"];
          // Focus the marker on the center of the screen
          map.flyTo({ center: e.features[0].geometry.coordinates });
        });
      });
    });
  });
</script>
