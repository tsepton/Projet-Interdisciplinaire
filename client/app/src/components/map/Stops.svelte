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

  $: stopId, stopModes, filter(stopId);
  $: stopModes, console.log(stopModes);

  function filter() {
    if (!map.isStyleLoaded()) return;
    map.setFilter("layer-stops", null);
    filterId();
    filterMode();
  }

  function filterId() {
    if (stopId && stopId.length > 0) {
      map.setFilter("layer-stops", ["==", "stop_id", stopId]);
    }
  }

  function filterMode() {
    if (stopModes && stopModes.length > 0) {
      stopModes.forEach((mode) => {
        map.setFilter("layer-stops", ["==", "mode", mode]);
      });
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
            "icon-image": "metro-marker",
            "text-field": ["get", "alpha_fr"],
            "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
            "text-offset": [0, 1.25],
            "text-anchor": "top",
          },
        });

        // Change the cursor to a pointer when the mouse is over the places layer.
        map.on("mouseenter", "layer-stops", (e) => {
          map.getCanvas().style.cursor = "pointer";
          // Filter lines and remove other stop markers
          dispatch("select", {
            ligne: e.features[0].properties["numero_lig"],
          });
          stopId = e.features[0].properties["stop_id"];
        });

        // Change it back to a pointer when it leaves.
        map.on("mouseleave", "layer-stops", (e) => {
          map.getCanvas().style.cursor = "";
          // Remove the  lines filter and re add other stop markers
          dispatch("select", { ligne: "null" });
          stopId = "";
        });

        // // When a click event occurs on a feature in the places layer, open a popup at the
        // // location of the feature, with description HTML from its properties.
        // map.on("click", "layer-stops", (e) => {
        //   // FIXME : Find proper information to visualise
        //   var coordinates = e.features[0].geometry.coordinates.slice();
        //   const description = e.features[0].properties.alpha_fr;
        //   // Ensure that if the map is zoomed out such that multiple
        //   // copies of the feature are visible, the popup appears
        //   // over the copy being pointed to.
        //   while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
        //     coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
        //   }
        //   new mapbox.Popup()
        //     .setLngLat(coordinates)
        //     .setHTML(description)
        //     .addTo(map);
        // });
      });
    });
  });
</script>
