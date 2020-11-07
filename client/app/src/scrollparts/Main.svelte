<script>
  import Map from "../components/map/Map.svelte";
  import Context from "../components/map/Context.svelte";
  import Stops from "../components/map/Stops.svelte";
  import Lines from "../components/map/Lines.svelte";
  import Filters from "../components/map/Filters.svelte";

  let stopFilter = "";
  let lineFilter = "";

  function filterLines(e) {
    lineFilter = e.detail.ligne
  }

  $: lineFilter, stopFilter, console.log(lineFilter, stopFilter)
</script>

<Context>
  <Map latitude={50.842912} longitude={4.377492} zoom={10.3}>
    <Lines filter={lineFilter} />
    <Stops bind:filter={stopFilter} on:select={filterLines} />
  </Map>
  <Filters bind:filter={stopFilter} />
</Context>
