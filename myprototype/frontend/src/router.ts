import axios from 'axios'
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import AllTestPage from './screens/AllTestPage.vue'
import Home from './screens/HomePage.vue'
import LastTestPage from './screens/LastTestPage.vue'
import LoginPage from './screens/LoginPage.vue'
import NewTestPage from './screens/NewTestPage.vue'
import RegisterPage from './screens/RegisterPage.vue'

const routes: RouteRecordRaw[] = [
	{
		path: '/',
		name: 'Home',
		component: Home,
		meta: {
			requiresAuth: true,
		},
	},
	{
		path: '/new-test',
		name: 'New Test',
		component: NewTestPage,
		meta: {
			requiresAuth: true,
		},
	},
	{
		path: '/last-test',
		name: 'Last Test',
		component: LastTestPage,
		meta: {
			requiresAuth: true,
		},
	},
	{
		path: '/all-test',
		name: 'All Test',
		component: AllTestPage,
		meta: {
			requiresAuth: true,
		},
	},
	{
		path: '/login',
		name: 'Login',
		component: LoginPage,
	},
	{
		path: '/register',
		name: 'Register',
		component: RegisterPage,
	},
]

const router = createRouter({
	history: createWebHistory(),
	routes,
})

const isAuthenticated = async (): Promise<boolean | undefined> => {
	try {
		const response = await axios.get('/api/auth/check', {
			withCredentials: true,
			headers: {
				'X-CSRF-TOKEN':
					document
						.querySelector('meta[name="csrf-token"]')
						?.getAttribute('content') || '',
			},
		})
		if (response.status === 201) {
			return true
		}
		return false
	} catch (err) {
		console.error(err)
	}
}

router.beforeEach(async (to, _from, next) => {
	if (to.matched.some(route => route.meta?.requiresAuth)) {
		if (await isAuthenticated()) {
			next()
		} else {
			next('/login')
		}
	} else {
		next()
	}
})

export default router
