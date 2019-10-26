import { Song } from './../models/song';
import { SongService } from './../services/song.service';
import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-song-detail',
  templateUrl: './song-detail.component.html',
  styleUrls: ['./song-detail.component.css']
})
export class SongDetailComponent implements OnInit {
  @Input() song: Song

  constructor(  private route: ActivatedRoute,
                private service: SongService) { }

  ngOnInit(): void {
    this.getSong();
  }
  
  getSong(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.service.getSong(id)
      .subscribe(song => this.song = song);
  }

}
