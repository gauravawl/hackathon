import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';
@Injectable()
export class NewsService {

  private result;

  
  constructor(private http: Http) { }


  getResult (news) {
    console.log(news);
    var url = `${"http://ec2-13-127-133-136.ap-south-1.compute.amazonaws.com:5000/webhook?news"}=${news}`;
    return this.http.get(url).map(result => this.result = result.json().data);
  }

}