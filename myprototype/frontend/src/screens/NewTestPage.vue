<script setup lang="ts">
import Dropdown from 'primevue/dropdown'
import FileUpload from 'primevue/fileupload'
import InputText from 'primevue/inputtext'
import Tag from 'primevue/tag'
import { onMounted, ref } from 'vue'
import ButtonComponent from '../components/ButtonComponent.vue'
import FilePreviewComponent from '../components/FilePreviewComponent.vue'
import Header from '../components/Header.vue'
import ResultPreviewComponent from '../components/ResultPreviewComponent.vue'
import { useTagsStore } from '../stores/tags.store'
import { useTestStore } from '../stores/test.store'

const tagsStore = useTagsStore()
const testStore = useTestStore()
const tags = ref()
const tests = ref()

onMounted(() => {
	tags.value = tagsStore.tags
	tests.value = testStore.tests
})

const addTags = () => {
	if (tag.value) {
		tagsStore.addTag(tag.value)
	}
}

const tag = ref<string>()
const name = ref('')
const fileInput = ref<HTMLInputElement | null>(null)
const file = ref()

const handleChangeFiles = () => {
	file.value = fileInput.value?.files
}

const selectedTest = ref()
</script>

<template>
	<Header />
	<main>
		<section>
			<div class="file_loading">
				<form>
					<FileUpload
						mode="basic"
						accept="image/*"
						:maxFileSize="1000000"
						:style="{
							width: '100%',
							height: '40px',
							'background-color': '#AEAEAE',
							'border-radius': '6px',
							border: 'none',
							color: '#000000',
							'font-size': '19px',
							outline: 'none',
						}"
						v-model="fileInput"
						upload-icon="none"
						choose-icon="none"
						choose-label="Загрузить файл"
						@change="handleChangeFiles()"
					/>
					<div class="name_field">
						<label for="name">Название</label>
						<InputText type="text" id="name" name="name" v-model="name" />
					</div>
					<div class="tags_field">
						<label for="tags">Теги</label>
						<div class="add_tags">
							<InputText
								type="text"
								id="tags"
								name="tags"
								:style="{ width: '100%' }"
								v-model="tag"
							/>
							<ButtonComponent
								label="Добавить"
								:style="{
									width: '150px',
								}"
								:disabled="tag === ''"
								@click="addTags()"
							/>
						</div>
						<div class="tags">
							<Tag
								v-for="(tag, index) in tags"
								:key="index"
								:value="tag"
								@remove="() => tagsStore.removeTag(tag)"
								:style="{
									'background-color': '#E4E4E4E4',
									color: '#000000',
									border: 'none',
									'font-size': '14px',
									outline: 'none',
									'border-radius': '6px',
									'max-width': '125px',
									height: '30px',
								}"
							/>
						</div>
					</div>
					<div class="test_chooser">
						<label for="test">Тест</label>
						<Dropdown
							id="test"
							name="test"
							v-model="selectedTest"
							:options="tests"
							option-label="name"
							placeholder="Выберите тест..."
							:style="{
								width: '100%',
								'background-color': '#E4E4E4',
								border: 'none',
								'font-size': '29px',
							}"
							dropdown-icon="pi pi-caret-right"
						/>
					</div>
					<ButtonComponent label="Запустить" type="submit" />
				</form>
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
	}
}

.file_loading {
	padding: 30px;
	> form {
		display: flex;
		flex-direction: column;
		gap: 20px;
		> .name_field {
			display: flex;
			flex-direction: column;
			gap: 10px;
			font-size: 20px;
			color: #000000;
		}
		> .tags_field {
			display: flex;
			flex-direction: column;
			gap: 10px;
			font-size: 20px;
			color: #000000;
			> .add_tags {
				display: flex;
				gap: 15px;
				width: 100%;
			}
			> .tags {
				display: flex;
				flex-wrap: wrap;
				gap: 10px;
			}
		}
		> .test_chooser {
			display: flex;
			flex-direction: column;
			gap: 10px;
			font-size: 20px;
			color: #000000;
		}
	}
}

.result_preview {
	display: grid;
	grid-template-columns: repeat(3, 1fr);
	height: 185px;
	> div {
		border-right: 1px solid #aeaeae;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		font-size: 20px;
		color: #000000;
		text-align: center;
		> h1 {
			font-size: 50px;
			font-weight: 400;
		}
	}
	> div:last-child {
		border-right: none;
	}
}
</style>
