<script>
  import { createEventDispatcher } from "svelte";
  import { fly } from "svelte/transition";
  const dispatch = createEventDispatcher();
  function close() {
    dispatch("close");
  }
</script>

<style>
  .container {
    position: absolute;
    z-index: 100 !important;
    max-height: 100%;
    margin: 0;

    background-color: #fff;
    color: rgba(0, 0, 0, 0.5);
    box-shadow: 0 0 5px 2px var(--secondary);
    border-radius: 3px;
    padding: 5px;
  }
  /* Small screens */
  @media (max-width: 900px) {
    .container {
      width: auto;
      padding: 10px;
      top: 2px;
      right: 2px;
      left: 2px;
      max-height: 85%;
      overflow: scroll;
      /* Hide scrollbar for IE, Edge and Firefox */
      -ms-overflow-style: none; /* IE and Edge */
      scrollbar-width: none; /* Firefox */
    }
    /* Hide scrollbar for Chrome, Safari and Opera */
    .container::-webkit-scrollbar {
      display: none;
    }
  }
  /* Larger screens */
  @media (min-width: 900px) {
    .container {
      width: 25%;
      top: 10px;
      right: 10px;
    }
  }
  hr {
    border: transparent;
    border-top: 0.01rem dashed grey;
    margin-bottom: 1.2rem;
  }
</style>

<div class="container" transition:fly={{ y: 50, duration: 250 }}>
  <slot name="title" />
  <hr />
  <slot name="body" />
</div>
