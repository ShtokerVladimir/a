import { defineStore } from 'pinia'

export const useTagsStore = defineStore('tags', {
	actions: {
		addTag(tag: string) {
			this.tags.push(tag)
			localStorage.setItem('tags', JSON.stringify(this.tags))
		},
		removeTag(tag: string) {
			this.tags = this.tags.filter(t => t !== tag)
			localStorage.setItem('tags', JSON.stringify(this.tags))
		},
	},
	getters: {},
	state: () => ({
		tags: [] as string[],
	}),
})
