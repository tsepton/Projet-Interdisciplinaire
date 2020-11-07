<script>
  import { getContext } from "svelte";
  import { key } from "../../lib/mapbox.js";

  const { getMap, getLines, getLayers } = getContext(key);
  const map = getMap();
  const lines = getLines();

  let layerIDs = [];

  //TODO in a sveltier way gros
  var filterInput = document.getElementById("filter-input");

  map.on("load", () => {
    lines.features.forEach((line) => {
      const id = `line-${line.properties["LIGNE"]}-${line.properties["VARIANTE"]}`;
      map.addSource(`line-${id}`, {
        type: "geojson",
        data: line,
      });

      if (!map.getLayer(id)) {
        map.addLayer({
          id: id,
          type: "line",
          source: `line-${id}`,
          layout: {
            "line-join": "round",
            "line-cap": "round",
          },
          paint: {
            "line-color": "#5B6886", //line.properties["COLOR_HEX"],
            "line-width": 1.7,
          },
        });
        layerIDs = [...layerIDs, id];
      }
    });

    filterInput.addEventListener("keyup", function (e) {
      // If the input value matches a layerID set
      // it's visibility to 'visible' or else hide it.
      var value = e.target.value.trim().toLowerCase();
      layerIDs.forEach((layerID) => {
        map.setLayoutProperty(
          layerID,
          "visibility",
          layerID.indexOf(value) > -1 ? "visible" : "none"
        );
      });
    });
  });
</script>
