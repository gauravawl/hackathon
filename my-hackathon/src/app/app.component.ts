import { Component } from '@angular/core';
import { NewsService } from './news.service';
import { Response } from '@angular/http/src/static_response';
import { Http } from '@angular/http';

import { map } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  outputFlag = false;
  title = 'Fake news Detection';
  result = '';
  probability = '';
  high = new Array();
  min = new Array();
  some = new Array();
  input = {
    newsText: ""
  };
  response = {};
  sens = '';
  error = '';

  constructor(private newsService: NewsService, private http: Http) {
  }


  search() {
    this.newsService.getResult(this.input.newsText).subscribe(response => {
      console.log(response);

      if (response["ERROR"]) {
        this.error = response["ERROR"];
        this.outputFlag = false;
        return;
      }

      this.result = response["RESULT"][0][0];
      this.probability = response["RESULT"][0][1][0];

      if (this.result) {
        this.outputFlag = true;
      }

      this.high = response["HIGH"];
      this.some = response["SOME"];
      this.min = response["MINIMAL"];

      if (response["SENS"] && response["SENS"] == 1)
        this.sens = 'Sensational';
      else
        this.sens = 'Objective';

      
    });
  }
  
}
