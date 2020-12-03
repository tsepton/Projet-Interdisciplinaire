<script>
  import Switch from "./Switch.svelte";
  
  export let name = "";
  export let modes = [];

  function handleMode(checked, ref) {
    if (checked) modes = [...modes, ref];
    else modes = [...modes.filter((elem) => elem !== ref)];
  }
</script>

<style>
  .container {
    width: 100%;
    margin: 0;
    position: absolute;
    z-index: 100 !important;

    background-color: #fff;
    color: rgba(0, 0, 0, 0.5);
    box-shadow: 0 0 5px 2px var(--secondary);
    border-radius: 3px;

    padding: 5px;
  }
  .ctrl .card {
    width: 100%;
  }
  .ctrl input[type="text"] {
    width: 100%;
    border-radius: 3px;
  }
  /* Small screens */
  @media (max-width: 900px) {
    .container {
      width: auto;
      padding: 10px;
      top: 2px;
      right: 2px;
      left: 2px;
    }
  }
  /* Large screens */
  @media (min-width: 900px) {
    .container {
      width: 25%;
      top: 10px;
      right: 10px;
    }
  }
</style>

<div class="container">
  <div class="ctrl">
    <input
      id="input"
      type="text"
      name="name"
      placeholder="Chercher une station..."
      bind:value={name} />
  </div>

  <div class="ctrl">
    <div class="card">
      <Switch
        checked={modes.includes('M') ? true : false}
        on:toggle={(e) => handleMode(e.detail.checked, 'M')}>
        Metro
      </Switch>
      <Switch
        checked={modes.includes('B') ? true : false}
        on:toggle={(e) => handleMode(e.detail.checked, 'B')}>
        Bus
      </Switch>
    </div>
  </div>
</div>
