<script>
  import { getContext } from "svelte";
  import { key } from "../../lib/mapbox.js";

  export let filter;
  export let mode;

  const { getMap, getLines } = getContext(key);
  const map = getMap();
  const lines = getLines();

  let layerIds = [];

  function filterLines(filter) {
    // If the input value matches a layerID set
    // it's visibility to 'visible' or else hide it.
    const value = `${(filter ?? "").toString()}${(mode ?? "").toLowerCase()}`;
    console.log(value);
    layerIds.forEach((layerId) => {
      let visibility = "none";
      if (value.length > 1 && layerId.indexOf(value) > -1)
        visibility = "visible";
      map.setLayoutProperty(layerId, "visibility", visibility);
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
      const layerID = `${ligneID}`;

      if (!layerIds.includes(layerID)) {
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
        layerIds = [...layerIds, layerID];
      }
    });
  });
</script>
