var React = require("react");
var StateFromStoreMixin = require("items-store/StateFromStoresMixin");
var RouteHandler = require("react-router").RouteHandler;
var Footer = require("./../components/Footer");
var Header = require("./../components/Header");
import Grid from "react-bootstrap/Grid";

// Styles
require("../styles/index.less");

var Application = React.createClass({
  render: function() {
    return (
      <Grid>
        <RouteHandler />
      </Grid>
    );
  }
});
module.exports = Application;
