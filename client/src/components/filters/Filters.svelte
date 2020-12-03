<script>
  import Switch from "./Switch.svelte";
  import Container from "./Container.svelte";

  export let isOpen;
  export let name = "";
  export let modes = [];

  function handleMode(checked, ref) {
    if (checked) modes = [...modes, ref];
    else modes = [...modes.filter((elem) => elem !== ref)];
  }
</script>

{#if isOpen}
  <Container>
    <h3 slot="title">Apply some filters...</h3>
    <div slot="body">
      <input
        id="input"
        type="text"
        name="name"
        placeholder="Chercher une station..."
        bind:value={name} />
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
  </Container>
{/if}
