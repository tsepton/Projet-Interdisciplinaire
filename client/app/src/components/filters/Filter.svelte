<script>
  export let features;
  export let key;
</script>

<style>
</style>

<div class="dropdown-filter">
  <label class="dropdown" for="stop-select"><slot name="title" /></label>
  <select name="points" id="stop-select">
    {#each features as feature}
      <option value={feature.properties[key]}>
        {feature.properties[key]}
      </option>
    {/each}
  </select>
</div>
