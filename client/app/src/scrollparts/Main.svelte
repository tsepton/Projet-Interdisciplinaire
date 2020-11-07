<script>
  import Map from "../components/map/Map.svelte";
  import Context from "../components/map/Context.svelte";
  import Stops from "../components/map/Stops.svelte";
  import Lines from "../components/map/Lines.svelte";
  import Filters from "../components/map/Filters.svelte";

  let filter = "";
</script>

<Context>
  <Map latitude={50.842912} longitude={4.377492} zoom={10.3}>
    <Lines />
    <Stops {filter} />
  </Map>
  <Filters bind:filter />
</Context>
