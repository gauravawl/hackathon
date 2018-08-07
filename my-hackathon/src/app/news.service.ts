import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';
@Injectable()
export class NewsService {

  private result;

  
  constructor(private http: Http) { }


  getResult (news) {
    console.log(news);
    return this.http.get('/news').map(result => this.result = result.json().data);
  }

}
