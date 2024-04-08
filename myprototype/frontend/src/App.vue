<script setup lang="ts">
import { useToast } from 'primevue/usetoast'

const toast = useToast()

toast.add({ severity: 'error', summary: 'Error', detail: 'Please login' })
</script>

<template>
	<router-view v-slot="{ Component, route }">
		<transition name="fade" mode="out-in">
			<div :key="route.path">
				<component :is="Component" />
			</div>
		</transition>
	</router-view>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
	transition-duration: 0.3s;
	transition-property: opacity;
	transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
	opacity: 0;
}
.logo {
	height: 6em;
	padding: 1.5em;
	will-change: filter;
	transition: filter 300ms;
}
.logo:hover {
	filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
	filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
