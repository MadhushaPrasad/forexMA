import React, { Component } from 'react'
import logo from './logo.svg';
import './App.css';
import { startSocketIO } from "./service/socket";
import store from './redux/store'
import ActionViewComponent from './components/action_view_component';
import MarketPriceViewCompoennt from "./components/market_status_price_view_component";
import MarketNewsViewCompoennt from "./components/market_status_news_view_component";
import MarketQualitativeFactViewCompoennt from "./components/market_qualitative_facts_view_component";
import MarketQuantitativeFactViewCompoennt  from "./components/market_quantitative_facts_view_component";

class App extends Component {
  componentWillMount() {
    startSocketIO(store);
  }

  render() {
    return (
      <div className="container lg h-screen bg-black text-white">
        <ActionViewComponent />
        <MarketPriceViewCompoennt />
        <MarketNewsViewCompoennt />
        <MarketQuantitativeFactViewCompoennt />
        <MarketQualitativeFactViewCompoennt/>
      </div>

    );
  }
}

export default App;
