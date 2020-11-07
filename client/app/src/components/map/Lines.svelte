<script>
  import { getContext } from "svelte";
  import { key } from "../../lib/mapbox.js";

  const { getMap, getLines, getLayers } = getContext(key);
  const map = getMap();
  const lines = getLines();

  let layerIDs = [];

  map.on("load", () => {
    map.addSource("source-lines", {
      type: "geojson",
      data: lines,
    });

    lines.features.forEach((line) => {
      const ligneID = line.properties["LIGNE"];
      const ligneVariante = line.properties["VARIANTE"];
      const layerID = `line-${ligneID}-${ligneVariante}`;

      if (!layerIDs.includes(layerID)) {
        map.addLayer({
          id: layerID,
          type: "line",
          source: "source-lines",
          layout: {
            "line-join": "round",
            "line-cap": "round",
            visibility: "none", // We do not show the line until the user select a stop related to it
          },
          paint: {
            "line-color": "#5B6886", //line.properties["COLOR_HEX"],
            "line-width": 1.7,
          },
          filter: ["==", "LIGNE", ligneID],
        });
        layerIDs = [...layerIDs, layerID];
      }
    });

    // filterInput.addEventListener("keyup", function (e) {
    //   // If the input value matches a layerID set
    //   // it's visibility to 'visible' or else hide it.
    //   var value = e.target.value.trim().toLowerCase();
    //   layerIDs.forEach((layerID) => {
    //     map.setLayoutProperty(
    //       layerID,
    //       "visibility",
    //       layerID.indexOf(value) > -1 ? "visible" : "none"
    //     );
    //   });
    // });
  });
</script>
