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
  let stopModeSelection = "";
  let isOpen = false;

  $: lineIdSelection,
    stopIdSelection,
    (isOpen = lineIdSelection && stopIdSelection);

  // Thanks to their very understandable API :
  // M is for metro, T for train & B for bus
  let stopModes = ["M"];

  function handleSelection(e) {
    lineIdSelection = e.detail.line;
    stopIdSelection = e.detail.stop;
    stopNameSelection = e.detail.name;
    stopModeSelection = e.detail.mode;
  }
</script>

<Context>
  <Map latitude={50.842912} longitude={4.377492} zoom={11}>
    <Lines filter={lineIdSelection} mode={stopModeSelection} />
    <Stops
      name={stopNameSelection}
      modes={stopModes}
      on:select={handleSelection} />
  </Map>
  <div>
    <Filters
      isOpen={!isOpen}
      bind:modes={stopModes}
      bind:name={stopNameSelection} />
    <Information
      {isOpen}
      lineId={lineIdSelection}
      stopId={stopIdSelection}
      stopName={stopNameSelection} />
  </div>
</Context>
