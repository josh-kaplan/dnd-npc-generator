var React = require("react");
//var Link = require("react-router").Link;
var NpcData = require("./../components/NpcData");
var Footer = require("./../components/Footer");
var Header = require("./../components/Header");
var UserInput = require("./../components/UserInput");
var Panel = require("react-bootstrap/Panel");
var Row = require("react-bootstrap/Row");
var Col = require("react-bootstrap/Col");

var actions = require("./../actions");

require("./index.less");

export default class DisplayNpc extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <Row>
          <Col
            xs={12}
            xsOffset={0}
          >
            <Header />
            <br />
            <Panel header="Notice of URL Change of this Website">
              NPC Generator has moved to a new domain.
              <br />
              Please use the address <a href="http://www.npcgenerator.com/">
                www.npcgenerator.com
              </a> to keep using this website.
            </Panel>
            <Footer />
          </Col>
        </Row>
      </div>
    );
  }
}
