import { Component } from '@angular/core';
import { NewsService } from './news.service';
import { Response } from '@angular/http/src/static_response';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Fake news Detection';

  input = {
    newsText: ""
  };
  
  constructor(private newsService: NewsService) {
  }

  search() {
    this.newsService.getResult(this.input.newsText).subscribe(response => {
      console.log(response);

    });
  }
  
}
