import axios from 'axios'
import { defineStore } from 'pinia'

export const useApiStore = defineStore('api', {
	actions: {
		async login(payload: LoginPayload) {
			this.isLoading = true
			const response = await axios.post('/api/auth/login', payload, {
				withCredentials: true,
				headers: {
					'X-CSRF-TOKEN':
						document
							.querySelector('meta[name="csrf-token"]')
							?.getAttribute('content') || '',
				},
			})
			if (response.status === 200) {
				this.isLoading = false
				this.isLoggedIn = true
				window.location.href = '/'
				return response.data
			}
			this.isLoading = false
			this.isLoggedIn = false
			this.errors.set('login', response.data)
			return response.data
		},
		async checkLogin() {
			const response = await axios.get('/api/auth/check', {
				withCredentials: true,
				headers: {
					'X-CSRF-TOKEN':
						document
							.querySelector('meta[name="csrf-token"]')
							?.getAttribute('content') || '',
				},
			})
			if (response.status === 200) {
				this.isLoggedIn = true
				return response.data
			}
			this.isLoggedIn = false
			return response.data
		},
	},
	state: () => ({
		isLoggedIn: false,
		isLoading: false,
		errors: new Map(),
	}),
})

interface LoginPayload {
	username: string
	password: string
}
