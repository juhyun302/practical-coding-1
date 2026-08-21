package com.ajou.prcoding.myweb.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.ajou.prcoding.myweb.entity.FavoriteMusic;
import java.util.List;

public interface FavoriteRepository extends JpaRepository<FavoriteMusic, String> {
    List<FavoriteMusic> findAll();

    void deleteById(String id);
}
