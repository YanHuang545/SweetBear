<template>
  <article class="candy" @click="$emit('open', item)">
    <img v-if="item.picUrl" :src="item.picUrl" :alt="item.title" />
    <div v-else class="ph">🍬</div>
    <div class="candy-body">
      <div class="price">¥ {{ item.price || "-" }}</div>
      <p>{{ shortTitle }}</p>
      <div class="meta">{{ item.area || "未知城市" }}</div>
    </div>
  </article>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  item: { type: Object, required: true },
});
defineEmits(["open"]);

const shortTitle = computed(() => {
  const title = props.item.title || "";
  return title.length > 36 ? title.slice(0, 36) + "…" : title;
});
</script>
