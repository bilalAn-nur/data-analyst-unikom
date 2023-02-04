import { Box, Button } from "@mui/material";
import Header from "../../components/Header";
import BarChart from "../../components/BarChart";
const Bar = () => {
  return (
    <Box m="20px">
      <Header title="Bar Chart" subtitle="Simple Bar Chart" />
      <Box height="60vh">
        <BarChart />
      </Box>
      <Box height="4vh">
        <Button type="submit" color="secondary" variant="contained">
          Generation 1 JP
        </Button>
        <Button type="submit" color="secondary" variant="contained">
          Generation 1 JP
        </Button>
      </Box>
    </Box>
  );
};

export default Bar;
