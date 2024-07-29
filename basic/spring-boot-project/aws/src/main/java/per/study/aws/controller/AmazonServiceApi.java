package per.study.aws.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import per.study.aws.service.AmazonService;

@RestController
public class AmazonServiceApi {

    private final AmazonService amazonService;

    public AmazonServiceApi(AmazonService amazonService) {
        this.amazonService = amazonService;
    }

    @GetMapping("/amazon")
    public void amazon() {
        amazonService.getCredentials();
    }
}
