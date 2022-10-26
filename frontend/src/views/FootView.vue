<template>
  <div
    class="relative bg-gray-50 pt-16 pb-20 px-4 sm:px-6 lg:pt-24 lg:pb-28 lg:px-8"
  >
    <div class="absolute inset-0">
      <div class="bg-white h-1/3 sm:h-2/3" />
    </div>
    <div class="relative max-w-7xl mx-auto">
      <div class="text-center">
        <h2
          class="text-3xl tracking-tight font-extrabold text-gray-900 sm:text-4xl"
        >
          From the food
        </h2>
        <p class="mt-3 max-w-2xl mx-auto text-xl text-gray-500 sm:mt-4">
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsa libero
          labore natus atque, ducimus sed.
        </p>
      </div>
      <div
        class="mt-12 max-w-lg mx-auto grid gap-5 lg:grid-cols-3 lg:max-w-none"
      >
        <div
          v-for="foot in APIData"
          :key="foot.id"
          class="flex flex-col rounded-lg shadow-lg overflow-hidden"
        >
          <router-link
            :to="{
              name: 'footDetail',
              params: {
                id: foot.id,
              },
            }"
          >
            <p>{{ foot.name }}</p>
          </router-link>
          {{ foot.description }}
          <img
            :src="'http://127.0.0.1:8000' + foot.picture"
            :alt="foot.picture"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { getAPI } from "../axios-api";
export default {
  name: "FootView",
  data() {
    return {
      APIData: [],
    };
  },
  created() {
    getAPI
      .get("/foot/foots/")
      .then((response) => {
        console.log("Post API has recieved data");
        this.APIData = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
