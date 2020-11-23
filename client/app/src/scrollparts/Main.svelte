<script>
  import Map from "../components/map/Map.svelte";
  import Context from "../components/map/Context.svelte";
  import Stops from "../components/map/Stops.svelte";
  import Lines from "../components/map/Lines.svelte";
  import Filters from "../components/filters/Filters.svelte";

  // TODO : Refactor ninja code, j'ai pas le temps maintenant gros

  let stopFilterName = "";
  let lineFilterNumber = "";

  // Thanks to their very understandable API :
  // M is for metro, T for train & B for bus
  let stopModes = ["M"];

  function filterLines(e) {
    lineFilterNumber = e.detail.ligne;
  }
</script>

<Context>
  <Map latitude={50.842912} longitude={4.377492} zoom={11}>
    <Lines filter={lineFilterNumber} />
    <Stops
      bind:filterName={stopFilterName}
      on:select={filterLines}
      {stopModes} />
  </Map>
  <Filters bind:modes={stopModes} bind:name={stopFilterName} />
</Context>
