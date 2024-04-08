<script setup lang="ts">
import Calendar from 'primevue/calendar'
import { onMounted, ref } from 'vue'
import FilePreviewComponent from '../components/FilePreviewComponent.vue'
import Header from '../components/Header.vue'
import ResultPreviewComponent from '../components/ResultPreviewComponent.vue'
import { useTestStore } from '../stores/test.store'

const testStore = useTestStore()
const tests = ref()

onMounted(() => {
	tests.value = testStore.tests
})

const date = ref()
</script>

<template>
	<Header />
	<main>
		<section>
			<h1>Список тестирований</h1>
			<div class="test_list">
				<div>
					<div>Название</div>
					<Calendar
						:style="{
							width: '100%',
							height: '30px',
							'border-radius': '0px',
							outline: 'none',
							border: 'none',
							'box-shadow': 'none',
						}"
						v-model="date"
						placeholder="Дата и время"
						showTime
						hourFormat="24"
					/>
					<div>Результат</div>
				</div>
				<div v-for="(test, index) in tests" :key="index" class="test_view">
					<div>{{ test.name }}</div>
					<div>{{ test.date }}</div>
					<div>{{ test.result }}</div>
				</div>
			</div>
		</section>
		<section>
			<ResultPreviewComponent />
			<FilePreviewComponent />
		</section>
	</main>
</template>

<style scoped>
main {
	display: grid;
	grid-template-columns: repeat(2, 1fr);
	height: calc(100vh - 60px);
	padding: 0 360px;
	gap: 20px;
	> section {
		width: 100%;
		display: flex;
		flex-direction: column;
		gap: 12px;
		margin-block: 25px;
		> div {
			width: 100%;
			border: 1px solid #aeaeae;
			border-radius: 6px;
		}
		> h1 {
			font-size: 24px;
			font-weight: 400;
		}
		> .test_list {
			display: grid;
			height: 100%;
			grid-auto-rows: 30px;
			> div {
				display: grid;
				grid-template-columns: repeat(3, 1fr);
				> div {
					display: flex;
					align-items: center;
					padding-left: 8px;
					border-right: 1px solid #aeaeae !important;
					border-bottom: 1px solid #aeaeae !important;
				}
				> div:nth-last-child(2) {
					padding-left: 0px;
				}
				> div:last-child {
					border-right: none !important;
				}
			}
		}
		> .test_view {
			display: grid;
			grid-template-columns: repeat(3, 1fr);
			> div {
				display: flex;
				font-size: 18px;
				align-items: center;
				border-right: 1px solid #aeaeae !important;
				border-bottom: 1px solid #aeaeae !important;
			}
		}
	}
}
</style>
