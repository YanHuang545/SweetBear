<template>
  <article class="goods" @click="$emit('open', item)">
    <div class="goods-cover">
      <img
        v-if="src"
        :src="src"
        :alt="item.title"
        :loading="priority ? 'eager' : 'lazy'"
        :fetchpriority="priority ? 'high' : 'low'"
        decoding="async"
        referrerpolicy="no-referrer"
        @error="onError"
      />
      <div v-else class="ph">无图</div>
      <span class="goods-hi">想带回家</span>
    </div>
    <div class="goods-body">
      <p class="goods-title">{{ item.title || "未命名商品" }}</p>
      <div class="goods-foot">
        <span class="price">¥ {{ item.price || "-" }}</span>
        <span class="meta">{{ item.area || "未知" }}</span>
      </div>
    </div>
  </article>
</template>

<script setup>
import { ref, watch } from "vue";
import { thumbUrl } from "../image";

const props = defineProps({
  item: { type: Object, required: true },
  priority: { type: Boolean, default: false },
});
defineEmits(["open"]);

const src = ref(thumbUrl(props.item.picUrl));
const triedOriginal = ref(false);

watch(
  () => props.item.picUrl,
  (url) => {
    src.value = thumbUrl(url);
    triedOriginal.value = false;
  },
);

function onError() {
  if (!triedOriginal.value && props.item.picUrl && src.value !== props.item.picUrl) {
    triedOriginal.value = true;
    src.value = props.item.picUrl;
    return;
  }
  src.value = "";
}
</script>
