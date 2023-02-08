import { ResponsivePie } from "@nivo/pie";
import { tokens } from "../theme";
import { useTheme } from "@mui/material";
import axios from "axios";
import React, { useState, useEffect } from "react";

const PieChart = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("/api/agensi").then((res) => setData(res.data));
  }, []);
  return (
    <ResponsivePie
      data={data}
      theme={{
        axis: {
          domain: {
            line: {
              stroke: colors.grey[100],
            },
          },
          legend: {
            text: {
              fill: colors.grey[100],
            },
          },
          ticks: {
            line: {
              stroke: colors.grey[100],
              strokeWidth: 1,
            },
            text: {
              fill: colors.grey[100],
            },
          },
        },
        legends: {
          text: {
            fill: colors.grey[100],
          },
        },
        tooltip: {
          container: {
            background: "#ffffff",
            color: "#000000",
          },
        },
      }}
      enableArcLabels={data.nameEnglish}
      margin={{ top: 40, right: 80, bottom: 80, left: 80 }}
      innerRadius={0.5}
      padAngle={0.7}
      cornerRadius={3}
      activeOuterRadiusOffset={8}
      colors={{ scheme: "category10" }}
      borderWidth={1}
      borderColor={{
        from: "color",
        modifiers: [["darker", 0.2]],
      }}
      arcLinkLabelsSkipAngle={10}
      arcLinkLabelsTextColor={colors.grey[100]}
      arcLinkLabelsThickness={2}
      arcLinkLabelsColor={{ from: "color" }}
      arcLabelsSkipAngle={10}
      arcLabelsTextColor="#ffffff"
      legends={[
        {
          anchor: "right",
          direction: "column",
          justify: false,
          translateX: 0,
          translateY: 0,
          itemWidth: 100,
          itemHeight: 20,
          itemsSpacing: 0,
          symbolSize: 20,
          itemDirection: "left-to-right",
        },
      ]}
    />
  );
};

export default PieChart;
