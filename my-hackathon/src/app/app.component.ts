import { Component } from '@angular/core';
import { NewsService } from './news.service';
import { Response } from '@angular/http/src/static_response';
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
  input = {
    newsText: ""
  };
  
  constructor(private newsService: NewsService) {
  }

  search() {
    this.newsService.getResult(this.input.newsText).subscribe(response => {
      console.log(response);
      this.result = response["RESULT"][0][0];
      this.probability = response["RESULT"][0][0][0];

      if (this.result) {
        this.outputFlag = true;
      }

      this.high = response["HIGH"];


    });
  }
  
}
