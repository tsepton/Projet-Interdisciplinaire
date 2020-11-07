<script>
  import { onMount, getContext } from "svelte";
  import { key } from "../../lib/mapbox.js";

  export let filter;

  const { getMap, getStops } = getContext(key);
  const map = getMap();
  const stops = getStops();

  let layerIDs = [];
  let filterInput = document.getElementById("filter-input");

  $: filter.length, filterStops(filter);

  function filterStops(filter) {
    layerIDs.forEach((layerID) => {
      map.setLayoutProperty(
        layerID,
        "visibility",
        layerID.indexOf(filter.toLowerCase()) > -1 ? "visible" : "none"
      );
    });
  }

  onMount(async () => {
    map.on("load", () => {
      map.loadImage("/marker.32px.png", (error, image) => {
        if (error) throw error;
        // TODO Visu : Marker
        map.addImage("metro-marker", image);

        map.addSource("source-stops", {
          type: "geojson",
          data: stops,
        });

        stops.features.forEach((stop) => {
          const stopID = stop.properties["stop_id"];
          const stopName = stop.properties["alpha_fr"].toLowerCase();
          const layerID = `${stopName}`;

          if (!layerIDs.includes(layerID)) {
            map.addLayer({
              id: layerID,
              type: "symbol",
              source: "source-stops",
              layout: {
                "icon-image": "metro-marker",
                // get the title name from the source's "title" property
                "text-field": ["get", "alpha_fr"],
                "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
                "text-offset": [0, 1.25],
                "text-anchor": "top",
              },
              filter: ["==", "stop_id", stopID],
            });
            layerIDs = [...layerIDs, layerID];
          }
        });
      });
    });
  });
</script>
