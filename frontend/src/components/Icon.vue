<template>
  <svg
    class="icon"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="1.7"
    stroke-linecap="round"
    stroke-linejoin="round"
    aria-hidden="true"
  >
    <template v-if="name === 'home'">
      <path d="M4 11.2 12 4.4 20 11.2V20a1 1 0 0 1-1 1h-5.1v-5.5H10.1V21H5a1 1 0 0 1-1-1z" />
    </template>
    <template v-else-if="name === 'search'">
      <circle cx="11" cy="11" r="6.2" />
      <path d="m16.2 16.2 4 4" />
    </template>
    <template v-else-if="name === 'publish'">
      <rect x="4.2" y="4.2" width="15.6" height="15.6" rx="4" />
      <path d="M12 8.2v7.6M8.2 12h7.6" />
    </template>
    <template v-else-if="name === 'messages'">
      <path d="M5 6h14a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-7.2L7 21v-4H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2z" />
    </template>
    <template v-else-if="name === 'orders'">
      <path d="m4.5 8 7.5-3.6L19.5 8 12 11.6z" />
      <path d="M4.5 8v7.2L12 19v-7.4M19.5 8v7.2L12 19" />
    </template>
    <template v-else-if="name === 'me'">
      <circle cx="12" cy="13.2" r="5.4" />
      <circle cx="7.4" cy="8" r="2.1" />
      <circle cx="16.6" cy="8" r="2.1" />
      <path d="M10.4 14.8c.9.8 2.3.8 3.2 0" />
    </template>
    <template v-else-if="name === 'back'">
      <path d="M14.4 5.8 8.2 12l6.2 6.2" />
    </template>
    <template v-else-if="name === 'heart'">
      <path d="M12 19.2s-6.6-3.8-8.3-7.4C2.4 9.4 3.6 6.6 6.4 6.2c1.6-.2 3 .6 3.6 1.8.6-1.2 2-2 3.6-1.8 2.8.4 4 3.2 2.7 5.6C18.6 15.4 12 19.2 12 19.2z" />
    </template>
    <template v-else-if="name === 'bag'">
      <path d="M6.2 8.2h11.6l-.8 10.2a2 2 0 0 1-2 1.8H9a2 2 0 0 1-2-1.8z" />
      <path d="M9 8.2V7a3 3 0 0 1 6 0v1.2" />
    </template>
  </svg>
</template>

<script setup>
defineProps({
  name: { type: String, required: true },
});
</script>
