<script>
  import Map from "../components/map/Map.svelte";
  import Context from "../components/map/Context.svelte";
  import Stops from "../components/map/Stops.svelte";
  import Lines from "../components/map/Lines.svelte";
  import Filters from "../components/filters/Filters.svelte";
  import Information from "../components/filters/Information.svelte";

  // TODO : Refactor ninja code, j'ai pas le temps maintenant gros
  // Vu la deadline, je l'aurai jamais

  let stopNameSelection = "";
  let stopIdSelection = "";
  let lineIdSelection = "";
  let isOpen = false;

  $: lineIdSelection,
    stopIdSelection,
    (isOpen = lineIdSelection && stopIdSelection);

  // Thanks to their very understandable API :
  // M is for metro, T for train & B for bus
  let mode = "";

  function handleSelection(e) {
    lineIdSelection = e.detail.line;
    stopIdSelection = e.detail.stop;
    stopNameSelection = e.detail.name;
  }
</script>

<Context>
  <Map latitude={50.842912} longitude={4.377492} zoom={11}>
    <Lines filter={lineIdSelection} {mode} />
    <Stops name={stopNameSelection} {mode} on:select={handleSelection} />
  </Map>
  <div>
    <Filters isOpen={!isOpen} bind:mode bind:name={stopNameSelection} />
    <Information
      {isOpen}
      lineId={lineIdSelection}
      stopId={stopIdSelection}
      stopName={stopNameSelection} />
  </div>
</Context>
