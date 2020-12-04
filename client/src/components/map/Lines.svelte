<script>
  import { getContext } from "svelte";
  import { key } from "../../lib/mapbox.js";

  export let filter;
  export let mode;

  const { getMap, getLines } = getContext(key);
  const map = getMap();
  const lines = getLines();

  let layerIDs = [];

  function filterLines(filter) {
    // If the input value matches a layerID set
    // it's visibility to 'visible' or else hide it.
    const value = `${(filter ?? "").toString()}${(mode ?? "").toLowerCase()}`;
    layerIDs.forEach((layerID) => {
      let visibility = "none";
      if (value !== "" && layerID.indexOf(value) > -1) visibility = "visible";
      map.setLayoutProperty(layerID, "visibility", visibility);
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
      const layerID = `${ligneID}`;

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
