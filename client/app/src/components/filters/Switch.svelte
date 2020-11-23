<script>
  import { createEventDispatcher } from "svelte";

  export let checked = false;
  
  const dispatch = createEventDispatcher();
  
  $: checked, dispatch("toggle", { checked });
</script>

<style>
  .switch {
    position: relative;
    display: inline-block;
    width: 2.5rem;
    height: 1.5rem;
  }

  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }

  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    -webkit-transition: 0.2s;
    transition: 0.2s;
  }

  .slider:before {
    position: absolute;
    content: "";
    height: 1.2rem;
    width: 1.2rem;
    left: 0.1rem;
    bottom: 0.14rem;
    background-color: white;
    -webkit-transition: 0.2s;
    transition: 0.2s;
  }

  input:checked + .slider {
    background-color: var(--primary);
  }

  input:focus + .slider {
    box-shadow: 0 0 1px var(--primary);
  }

  input:checked + .slider:before {
    -webkit-transform: translateX(1.1rem);
    -ms-transform: translateX(1.1rem);
    transform: translateX(1.1rem);
  }

  /* Rounded sliders */
  .slider.round {
    border-radius: 34px;
  }

  .slider.round:before {
    border-radius: 50%;
  }
</style>

<slot />
<label class="switch">
  <input type="checkbox" {checked} on:click={() => (checked = !checked)} />
  <span class="slider round" />
</label>
