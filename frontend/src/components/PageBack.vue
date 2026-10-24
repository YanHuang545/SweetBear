<template>
  <button type="button" class="back-link" @click="go">
    <Icon name="back" />
    {{ label }}
  </button>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import Icon from "./Icon.vue";
import { lastItemPath, lastListPath } from "../session";

const props = defineProps({
  to: String,
  label: { type: String, default: "返回" },
});

const route = useRoute();
const router = useRouter();

function go() {
  if (props.to) {
    router.push(props.to);
    return;
  }
  const from = typeof route.query.from === "string" ? route.query.from : "";
  if (from.startsWith("/")) {
    router.push(from);
    return;
  }
  if (route.path === "/messages" || route.path === "/orders") {
    router.push(lastItemPath());
    return;
  }
  if (route.path.startsWith("/item")) {
    router.push(lastListPath());
    return;
  }
  router.push("/");
}
</script>
