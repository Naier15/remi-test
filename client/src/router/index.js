import { createRouter, createWebHistory } from 'vue-router'
import Menu from '@/components/Menu.vue'
import Basket from '@/components/Basket.vue'

const routes = [
  {
    path: '/vue',
    name: 'Menu',
    component: Menu
  },
  {
    path: '/vue/basket',
    name: 'Basket',
    component: Basket
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
