import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import SDGs from '../views/SDGs.vue'
import CarbonFootprint from '../views/CarbonFootprint.vue'
import ActNow from '../views/ActNow.vue'
import TeamSDGs from '../views/TeamSDGs.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About },
  { path: '/sdgs', name: 'SDGs', component: SDGs },
  { path: '/team-sdgs', name: 'TeamSDGs', component: TeamSDGs },
  { path: '/carbon-footprint', name: 'CarbonFootprint', component: CarbonFootprint },
  { path: '/act-now', name: 'ActNow', component: ActNow }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
