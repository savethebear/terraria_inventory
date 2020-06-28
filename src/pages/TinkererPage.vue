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
              <td>{{row.result}}</td>
              <td>
                <div v-for="ingredient in row.ingredients" :key="ingredient">
                  <img :src="ingredient.icon">
                  <div class="ingredient_content">{{ ingredient.ingredient }}</div>
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
                tableData: [
                  {
                    result: "Amber Horseshoe Balloon",
                    result_icon: "https://gamepedia.cursecdn.com/terraria_gamepedia/8/8e/Amber_Horseshoe_Balloon.png?version=f82cce573c254c2b2dee7341800e388f",
                    ingredients: [
                      {ingredient: "Lucky Horseshoe", icon: "https://gamepedia.cursecdn.com/terraria_gamepedia/d/d7/Lucky_Horseshoe.png?version=f31cd1c9751200c0ec303b6498332c2f"}, 
                      {ingredient: "Honey Balloon", icon: "https://gamepedia.cursecdn.com/terraria_gamepedia/b/b8/Honey_Balloon.png?version=c574998f0819b1b72730357e68bec330"}
                    ],
                  }
                ]
              }
            ]
        }
    }
}

</script>