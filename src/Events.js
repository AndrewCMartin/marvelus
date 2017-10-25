import React from 'react'
import { Link } from 'react-router-dom'

const Events = () => (
    <div class="container" style="margin-top:100px;">
          <div class="row">
            <div class="col-sm-4">
              <div class="panel panel-info">
                <div class="panel-heading"><a href="{{url_for('frontend.event', name='actsOfVengeance')}}">Acts of Vengeance!</a></div>
                {/* <div class="panel-body"><img src="https://i.annihil.us/u/prod/marvel/i/mg/3/b0/588b583ed0523/detail.jpg" class="img-responsive" style="width:100%" alt="Image"></a></div> */}
                <div class="panel-footer">
                  Acts of Vengeance!
                </div>
              </div>
            </div>
            <div class="col-sm-4">
              <div class="panel panel-danger">
                <div class="panel-heading"><a href="{{url_for('frontend.event', name='ageOfUltron')}}">Age of Ultron!</a></div>
                {/* <div class="panel-body"><img src="https://i.annihil.us/u/prod/marvel/i/mg/c/d0/51ed8cf71fd82/detail.jpg" class="img-responsive" style="width:100%" alt="Image"></a></div> */}
                <div class="panel-footer">
                    Age of Ultron!
                  </div>
              </div>
            </div>
            <div class="col-sm-4">
              <div class="panel panel-success">
                <div class="panel-heading"><a href="{{url_for('frontend.event', name='ageOfApocolypse')}}">Age of Apocolypse</a></div>
                {/* <div class="panel-body"><img src="https://i.annihil.us/u/prod/marvel/i/mg/7/00/599b1cf83439a/detail.jpg" class="img-responsive" style="width:100%" alt="Image"></a></div> */}
                <div class="panel-footer">
                    Age of Apocolypse
                  </div>
              </div>
            </div>
          </div>
        </div>
)

export default Events