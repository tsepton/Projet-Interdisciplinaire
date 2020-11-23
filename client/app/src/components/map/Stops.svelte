<script>
  import { onMount, getContext, createEventDispatcher } from "svelte";
  import { key } from "../../lib/mapbox.js";

  // TODO : filter based on name
  export let filterName;
  export let stopId;
  export let stopModes;

  const { getMap, getStops } = getContext(key);
  const map = getMap();
  const stops = getStops();
  const dispatch = createEventDispatcher();

  // FIXME: Best hack ever
  setTimeout(handleFilters, 2000);

  $: stopId, stopModes, handleFilters();

  function handleFilters() {
    if (!map.isStyleLoaded()) return;
    map.setFilter("layer-stops", null);
    map.setLayoutProperty("layer-stops", "visibility", "visible");
    filterMode();
    filterId();
  }

  function filterId() {
    if (stopId && stopId.length > 0) {
      map.setFilter("layer-stops", ["==", "stop_id", stopId]);
    }
  }

  function filterMode() {
    if (stopModes && stopModes.length) {
      // Gros code mon gars
      if (stopModes.length > 1) {
        map.setFilter("layer-stops", ["!=", "mode", "T"]);
      } else {
        map.setFilter("layer-stops", ["==", "mode", stopModes[0]]);
      }
    } else {
      map.setLayoutProperty("layer-stops", "visibility", "none");
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
          // TODO
          // cluster: true,
          // clusterMaxZoom: 10,
          // clusterRadius: 10,
          // maxzoom: 15,
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

        // Change it back to a pointer when it leaves.
        map.on("click", () => {
          map.getCanvas().style.cursor = "";
          // Remove the  lines filter and re add other stop markers
          dispatch("select", { ligne: "null" });
          stopId = "";
        });

        // When a click event occurs on a feature in the places layer, open a popup at the
        // location of the feature, with description HTML from its properties.
        map.on("click", "layer-stops", (e) => {
          map.getCanvas().style.cursor = "pointer";
          // Filter lines and remove other stop markers
          dispatch("select", {
            ligne: e.features[0].properties["numero_lig"],
          });
          stopId = e.features[0].properties["stop_id"];
        });
      });
    });
  });
</script>
