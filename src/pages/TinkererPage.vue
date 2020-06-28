<template>
  <div>
    <div class="row">
      <div class="col-12" v-for="table in tinkererData" :key="table.title">
        <card>
          <h4>{{ table.title }}</h4>
          <paper-table :data="table.tableData" :columns="table.tableColumns">
            <template slot="columns">
              <th>Result</th>
              <th>Ingredients</th>
            </template>
            <template slot-scope="{row}">
              <td>
                <img :src="row.result.img_src"/>
                <div class="ingredient_content">{{row.result.name}}</div>
              </td>
              <td>
                <div v-for="ingredient in row.ingredients" :key="ingredient.name">
                  <img :src="ingredient.img_src">
                  <div class="ingredient_content">{{ ingredient.name }}</div>
                </div>
              </td>
            </template>
          </paper-table>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
import { PaperTable } from "@/components/index";
import TinkerTools from "../data/tinker_recipes.json";
export default {
    components: {
        PaperTable
    },
    data() {
        return {
            HEADERS: ["result", "ingredients"],
            tinkererData: [
              {
                title: "Craftable Tools",
                tableColumns: ["Result", "Ingredients"],
                tableData: []
              }
            ]
        }
    },
    created() {
      this.tinkererData[0].tableData = TinkerTools;
    }
}

</script>