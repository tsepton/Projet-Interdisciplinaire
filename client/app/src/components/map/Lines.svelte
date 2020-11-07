<script>
  import { getContext } from "svelte";
  import { key } from "../../lib/mapbox.js";

  export let filter;

  const { getMap, getLines, getLayers } = getContext(key);
  const map = getMap();
  const lines = getLines();

  let layerIDs = [];

  function filterLines(filter) {
    // If the input value matches a layerID set
    // it's visibility to 'visible' or else hide it.
    var value = filter.toString();
    layerIDs.forEach((layerID) => {
      map.setLayoutProperty(
        layerID,
        "visibility",
        layerID.indexOf(value) > -1 ? "visible" : "none"
      );
    });
  }

  $: filter, filterLines(filter);

  map.on("load", () => {
    map.addSource("source-lines", {
      type: "geojson",
      data: lines,
    });

    lines.features.forEach((line) => {
      const ligneID = line.properties["LIGNE"];
      const ligneNumber = line.properties["LIGNE"];
      const ligneVariante = line.properties["VARIANTE"];
      const layerID = `line-${ligneID}:${ligneVariante}-${ligneNumber}`;

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
  });
</script>
