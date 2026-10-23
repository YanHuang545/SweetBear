import { createRouter, createWebHistory } from "vue-router";
import { getCookie } from "./session";
import Login from "./pages/Login.vue";
import Home from "./pages/Home.vue";
import Search from "./pages/Search.vue";
import Item from "./pages/Item.vue";
import Publish from "./pages/Publish.vue";
import Messages from "./pages/Messages.vue";
import Orders from "./pages/Orders.vue";
import Profile from "./pages/Profile.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/login", component: Login },
    { path: "/", component: Home, meta: { auth: true } },
    { path: "/search", component: Search, meta: { auth: true } },
    { path: "/item/:id", component: Item, meta: { auth: true } },
    { path: "/publish", component: Publish, meta: { auth: true } },
    { path: "/messages", component: Messages, meta: { auth: true } },
    { path: "/orders", component: Orders, meta: { auth: true } },
    { path: "/me", component: Profile, meta: { auth: true } },
  ],
  scrollBehavior() {
    return { top: 0 };
  },
});

router.beforeEach((to, from, next) => {
  const loggedIn = Boolean(getCookie());
  if (to.meta.auth && !loggedIn) next({ path: "/login", query: { redirect: to.fullPath } });
  else if (to.path === "/login" && loggedIn) next("/");
  else next();
});

export default router;
