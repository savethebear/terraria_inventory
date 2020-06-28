<template>
  <div>
    <div class="container">
      <div class="row justify-content-end">
        <p-button @click.native="triggerImport" type="info">Import Inventory Data</p-button>
        <input type="file" id="input" style="display:none;" @change="importData" />
      </div>
    </div>
    <div class="row">
      <div class="col-md-6 col-12" v-for="table in overviewData" :key="table.title">
        <card>
          <h4>{{ table.title }}</h4>
          <paper-table :data="table.tableData" :columns="table.tableColumns">
            <template slot="columns">
              <th>Item</th>
              <th>Quantity</th>
            </template>
            <template slot-scope="{row}">
              <td>{{row.item}}</td>
              <td>{{row.quantity}}</td>
            </template>
          </paper-table>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
import { PaperTable } from "@/components/index";
import { Button as PButton } from "@/components";
export default {
  components: {
    PaperTable,
    PButton
  },

  data() {
    return {
      HEADERS: ["item", "quantity"],
      overviewData: [
        {
          title: "Weapons",
          tableColumns: ["Item", "Quantity"],
          tableData: []
        }
      ]
    };
  },
  methods: {
    triggerImport() {
      document.getElementById("input").click();
    },
    convertJSON(csv) {
      const lines = csv.split("\n");
      const result = [];

      const headers = lines[0].split(",");
      if (!this.compareHeaders(headers)) {
        alert("Incorrect Headers...");
        return;
      }

      for (let i = 1; i < lines.length; i++) {
        const obj = {};
        const inputs = lines[i].split(",");
        let isValid = true;
        for (let j = 0; j < headers.length && isValid; j++) {
          if (!inputs[j]) {
            isValid = false;
          } else {
            obj[headers[j]] = inputs[j];
          }
        }
        if (isValid) {
          result.push(obj);
        }
      }

      return result;
    },
    compareHeaders(headers) {
      if (headers.length !== this.HEADERS.length) {
        return false;
      }

      for (let i = 0; i < headers.length; i++) {
        if (headers[i] !== this.HEADERS[i]) {
          return false;
        }
      }

      return true;
    },
    importData() {
      const file = document.getElementById('input').files[0];
      if (file.type === "text/csv") {
        let reader = new FileReader();
        const _this = this;
        reader.onloadend = function() {
          // TODO: Put items into buckets (tools, weapons, materials)
          _this.overviewData[0].tableData = _this.convertJSON(this.result);
        }
        reader.readAsText(file);
      } else {
        alert("invalid file type");
      }
    }
  }
};
</script>
<style>
</style>
