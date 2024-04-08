<script setup lang="ts">
import Dropdown from 'primevue/dropdown'
</script>
<template>
	<div class="files_preview">
		<div class="table">
			<div>Файлы</div>
			<Dropdown
				:options="[]"
				dropdown-icon="pi pi-caret-down"
				:style="{
					width: '100%',
					'border-radius': '0',
					outline: 'none',
					border: '1px solid #aeaeae',
				}"
				placeholder="Баллы"
			/>
			<div>Ссылка на ответ</div>
		</div>
		<div class="table_files">
			<div></div>
			<div></div>
			<div></div>
		</div>
	</div>
</template>
<style scoped>
.files_preview {
	height: 100%;
	> .table {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		width: 100%;
		height: 30px;
		> div {
			display: flex;
			align-items: center;
			height: 30px;
			padding-left: 8px;
			border-right: 1px solid #aeaeae;
			border-bottom: 1px solid #aeaeae;
		}
		> div:last-child {
			border-right: none;
		}
		> div:nth-last-child(2) {
			border-top: none !important;
			border-left: none !important;
			padding-left: 0px !important;
		}
	}
	> .table_files {
		width: 100%;
		height: calc(100% - 30px);
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		> div {
			display: flex;
			border-right: 1px solid #aeaeae;
		}
		> div:last-child {
			border-right: none;
		}
	}
}
</style>
