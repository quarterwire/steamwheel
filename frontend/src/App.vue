<script setup lang="ts">
import InputText from 'primevue/inputtext' // This component is unused in the template
import Button from 'primevue/button'
import { useFetch } from '@vueuse/core'
import { ref, watch } from 'vue'

export interface Game {
  type: string
  name: string
  steam_appid: number
  required_age: number
  is_free: boolean
  dlc: any
  detailed_description: string
  about_the_game: string
  short_description: string
  supported_languages: string
  header_image: string
  capsule_image: string
  capsule_imagev5: string
  website: string
  pc_requirements: PcRequirements
  mac_requirements: MacRequirements
  linux_requirements: LinuxRequirements
  legal_notice: string
  developers: string[]
  publishers: string[]
  price_overview: any
  packages: any[]
  platforms: Platforms
  metacritic: any
  categories: Category[]
  genres: Genre[]
  screenshots: Screenshot[]
  movies: Movie[]
  recommendations: any
  release_date: ReleaseDate
  background: string
  background_raw: string
  ratings: Ratings
}

export interface PcRequirements {
  minimum: string
  recommended: string
}

export interface MacRequirements {
  minimum: string
  recommended: string
}

export interface LinuxRequirements {
  minimum: string
  recommended: string
}

export interface Platforms {
  windows: boolean
  mac: boolean
  linux: boolean
}

export interface Category {
  id: number
  description: string
}

export interface Genre {
  id: string
  description: string
}

export interface Screenshot {
  id: number
  path_thumbnail: string
  path_full: string
}

export interface Movie {
  id: number
  name: string
  thumbnail: string
  webm: Webm
  mp4: Mp4
  dash_av1: string
  dash_h264: string
  hls_h264: string
  highlight: boolean
}

export interface Webm {
  '480': string
  max: string
}

export interface Mp4 {
  '480': string
  max: string
}

export interface ReleaseDate {
  coming_soon: boolean
  date: string
}

export interface Ratings {
  esrb: any
  kgrb: any
  pegi: any
  bbfc: any
  usk: any
  oflc: any
  nzoflc: any
  crl: any
}
const game = ref<Game | null>(null)
const API_URL = 'http://localhost:8000/random_game'

// 2. Use useFetch with immediate: true (to run on setup) and destructure 'execute'
const { isFetching, error, data, execute } = useFetch(API_URL, { immediate: true }).json() // Use .json() for automatic parsing

// 3. Define the function to call when the button is clicked
const getRandomGame = () => {
  console.log(data)
  execute()
}

// 4. Watch for changes in the raw 'data' Ref and safely update 'game'
watch(
  data,
  (newData) => {
    // The .json() option from useFetch automatically handles the JSON.parse,
    // so 'newData' is already the parsed object or null.
    if (newData) {
      // Cast it to our expected interface
      game.value = newData as Game
    } else {
      game.value = null
    }
  },
  { immediate: true },
)
</script>

<template>
  <div class="flex flex-col gap-6 items-center justify-center mx-auto container">
    <h1>Steam Wheel - get a random game</h1>

    <h1 v-if="isFetching">Loading game...</h1>

    <h1 v-else-if="error">Error: {{ error.message }}</h1>

    <h1 v-else-if="game">{{ game.name }}</h1>

    <h1 v-else>Click the button to fetch a game!</h1>
    <img v-if="!isFetching" v-bind:src="game?.screenshots[0]?.path_full || 'image.jpg'" />

    <Button @click="getRandomGame" :disabled="isFetching"> Get a random game </Button>
  </div>
</template>

<style scoped>
/* Your styles here */
</style>
