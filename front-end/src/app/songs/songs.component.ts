import { SongService } from './../services/song.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'songs',
  templateUrl: './songs.component.html',
  styleUrls: ['./songs.component.css']
})
export class SongsComponent implements OnInit {
  
  constructor(private service: SongService) { }

  ngOnInit() {
    this.service.getSongs().subscribe(
      response => console.log(response)
    )
  }

}
